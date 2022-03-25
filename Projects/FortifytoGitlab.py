import json
import xmltodict

gitlabResults = {
	"version": "14.0.4",
	"vulnerabilities": []
}

# Converts default Fortify SCA XML report to JSON file
def convertToXML():
	with open("test.xml") as xmlFile:
		loadedXML = xmltodict.parse(xmlFile.read())
		newJSONData = json.dumps(loadedXML, indent=4)
		with open("parsed.json", "w") as jfile:
			jfile.write(newJSONData)

# Handles information to return specific issues rather than full report
def generateResults():
	with open("parsed.json", 'r') as rawReport:
		jsonResults = json.load(rawReport)
		#Change values to be scalable if report is weird
		results = jsonResults['ReportDefinition']['ReportSection'][2]['SubSection'][1]['IssueListing']['Chart']['GroupingSection']
		return results

# Builds SAST report using GitLab JSON SAST format
def buildSASTReport(results):
	#Review checks for edge handling
	if results:
		for issues in results:
			coreInfo = issues['Issue']
			gitlabResults['vulnerabilities'].append({
					"id": issues['groupTitle'],
					"category": "fortify_sast", #may need to change to sast
					"message": issues['groupTitle'] + " in " + coreInfo['Primary']['FileName'] + " on line " + coreInfo['Primary']['LineStart'],
					"description": coreInfo['Abstract'],
					"severity": coreInfo['Friority'],
					"confidence": "Unknown",
					"solution": issues['MajorAttributeSummary']['MetaInfo'][2]['Value'],
					"scanner": {
						"id": "fortifycli",
						"name": "FortifySCA"
					},
					"location": {
						"file" : coreInfo['Primary']['FilePath'],
						"start_line": coreInfo['Primary']['LineStart'],
						"method": coreInfo['Primary']['TargetFunction'],
						"dependency": {
							"package": {}
						}
					},
					"identifiers": [
						{
						"type": "fortify_ruleID",
						"name": "@ruleID",
						"value": coreInfo['@ruleID'],
						#may need removal
						"snippet": coreInfo['Primary']['Snippet']
						}
					]
				})
	else:
		print("No results found.")

# Exports JSON to file for uploading to Security Dashboard
def exportGitLabReport():
	with open("report.json", 'w') as finalReport:
		finalReport.write(json.dumps(gitlabResults, indent=4))

convertToXML()
generateResults()
buildSASTReport(generateResults())
exportGitLabReport()
