import sys

def convert_command(sfdx_command):
    # Replace -u with -o
    sfdx_command = sfdx_command.replace(" -u ", " -o ")

    # Dictionary to map sfdx commands to sf commands
    command_map = {
        "alias:set": "alias set",
        "alias:unset": "alias unset",
        "alias:list": "alias list",
        "force:analytics:template:create": "analytics generate template",
        "force:apex:class:create": "apex generate class",
        "force:apex:trigger:create": "apex generate trigger",
        "force:apex:execute": "apex run",
        "force:apex:log:get": "apex get log",
        "force:apex:log:list": "apex list log",
        "force:apex:log:tail": "apex tail log",
        "force:apex:test:report": "apex get test",
        "force:apex:test:run": "apex run test",
        "force:cmdt:create": "cmdt generate object",
        "force:cmdt:field:create": "cmdt generate field",
        "force:cmdt:generate": "cmdt generate fromorg",
        "force:cmdt:record:create": "cmdt generate record",
        "force:cmdt:record:insert": "cmdt generate records",
        "force:community:create": "community create",
        "force:community:template:list": "community list template",
        "force:community:publish": "community publish",
        "config:get": "config get",
        "config:list": "config list",
        "config:set": "config set",
        "config:unset": "config unset",
        "force:data:record:create": "data create record",
        "force:data:bulk:delete": "data delete bulk",
        "force:data:bulk:status": "data delete resume",
        "force:data:record:delete": "data delete record",
        "force:data:tree:export": "data export tree",
        "force:data:record:get": "data get record",
        "force:data:tree:import": "data import tree",
        "force:data:soql:query": "data query",
        "force:data:soql:bulk:report": "data query resume",
        "force:data:bulk:status": "data resume",
        "force:data:record:update": "data update record",
        "force:data:bulk:upsert": "data upsert bulk",
        "force:data:bulk:status": "data upsert resume",
        "force:package:create": "package create",
        "force:package:delete": "package delete",
        "force:package:install": "package install",
        "force:package:install:report": "package install report",
        "force:package:install:list": "package install list",
        "force:package:list": "package list",
        "force:package:uninstall": "package uninstall",
        "force:package:uninstall:report": "package uninstall report",
        "force:package:update": "package update",
        "force:package:version:create": "package version create",
        "force:package:version:create:list": "package version create list",
        "force:package:version:create:report": "package version create report",
        "force:package:version:delete": "package version delete",
        "force:package:version:displayancestry": "package version displayancestry",
        "force:package:version:list": "package version list",
        "force:package:version:promote": "package version promote",
        "force:package:version:report": "package version report",
        "force:package:version:update": "package version update",
        "force:mdapi:convert": "project convert mdapi",
        "force:source:convert": "project convert source",
        "force:source:delete": "project delete source",
        "force:source:tracking:clear": "project delete tracking",
        "force:source:deploy:cancel": "project deploy cancel",
        "force:source:status": "project deploy preview",
        "force:source:deploy:report": "project deploy report",
        "force:source:deploy": "project deploy start",
        "force:project:create": "project generate",
        "force:source:manifest:create": "project generate manifest",
        "force:source:ignored:list": "project list ignored",
        "force:source:tracking:reset": "project reset tracking",
        "force:source:retrieve": "project retrieve start",
        "force:user:permset:generate": "org assign permset",
        "force:user:permsetlicense:generate": "org assign permsetlicense",
        "force:org:shape:create": "org create shape",
        "force:org:snapshot:create": "org create snapshot",
        "force:user:create": "org create user",
        "force:org:delete": "org delete sandbox",
        "force:org:delete": "org delete scratch",
        "force:org:shape:delete": "org delete shape",
        "force:org:snapshot:delete": "org delete snapshot",
        "force:user:display": "org display user",
        "force:org:display": "org display",
        "force:user:password:generate": "org generate password",
        "force:org:snapshot:get": "org get snapshot",
        "force:org:list": "org list",
        "auth:list": "org list auth",
        "force:mdapi:listmetadata": "org list metadata",
        "force:mdapi:describemetadata": "org list metadata-types",
        "force:org:shape:list": "org list shape",
        "force:org:snapshot:list": "org list snapshot",
        "force:user:list": "org list users",
        "auth:jwt:grant": "org login jwt",
        "auth:web:login": "org login web",
        "auth:accesstoken:store": "org login access-token",
        "auth:device:login": "org login device",
        "auth:sfdxurl:store": "org login sfdx-url",
        "auth:logout": "org logout",
        "force:org:open": "org open",
        "force:org:status": "org resume sandbox",
        "sfdx": "sf",
    }

       # Find and replace the sfdx command part with its sf equivalent
    for sfdx, sf in command_map.items():
        if sfdx in sfdx_command:
            sfdx_command = sfdx_command.replace(sfdx, sf)

    return sfdx_command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an sfdx command as an argument.")
    else:
        sfdx_command = sys.argv[1]
        sf_command = convert_command(sfdx_command)
        print(f"{sf_command}")
