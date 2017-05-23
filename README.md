# python-streaming-deserialisation-tools
Simple Python code for fetching and deserialising experiment data.

This is a simple set of tools for fetching data from Kafka and deserialising it - it is purely for diagnostic purposes.

The schemas for the various data-types are found in the following repository:
https://github.com/ess-dmsc/streaming-data-types
 
If the schema changes then new Python code will have to generated using flatc:

```flatc.exe -p -o "SchemaFolderName" "Schema.fbs"```
