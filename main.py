import os, json
def main():
    print("Hello, welcome to the automated workspace setup program, what profile would you like to use?: (If you have no profiles please read the instructions at )\n")
    with open("PythoLocalDirectoryAutomationScript\\workspaceConfigs.json", "r") as configFile:
        configData = json.load(configFile)
    for i, profileName in enumerate(configData["Profiles"]):
        print(f"{i}. {profileName["user"]}\n")
if __name__ == "__main__":
    main()
