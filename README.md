# PythoLocalDirectoryAutomationScripts
Python script which helps to automate repetitive tasks.

## Script 1, Workspaces:
Workspaces is a python automation script which automatically opens and closses certain "workspaces", or set of applications the user wants open or closed at a given time based on the workspace preferences input by the user. These workspaces are configured using the workspaceConfigs.json file which holds the all the relevant information on which processes, and in which grouping should be opened/closed at any given time.

### TLI Commands and Info 

### Workspace Configuration File
<img width="1423" height="903" alt="image" src="https://github.com/user-attachments/assets/60621855-244a-4cae-b4ea-2777a48e9fc1" />
> ***Example workspace config provided within the repository, it is recomended to use the file as a template to create your own workspaces, your configs will likely be and look different***

Within a config file is the large grouping of profiles, this grouping holds multiple users, each of which with their own workspaces and programs to open and close when finished. The hierarchy looks as follows:

- **Profiles**
  - **Users**
   - **Workspaces**

The code is based on the json file being of this structure so it is imperative to keep this structure 


