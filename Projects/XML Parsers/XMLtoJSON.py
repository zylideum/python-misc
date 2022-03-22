def convertXML():
	with open("test.xml") as xmlFile:
		loadedXML = xmltodict.parse(xmlFile.read())

		newJSONData = json.dumps(loadedXML, indent=1)
		with open("parsed.json", "w") as jfile:
			jfile.write(newJSONData)

convertXML()
