# Jira Automation Schematic Hybrid Framework
## Build Version: 1.0.0
### Framework: ![Author](https://img.shields.io/badge/Author-Deepak_Togloor-orange)
***
| About Framework                               | 
|-----------------------------------------------|
| __Framework Used__: Pytest                    | 
| __Design Pattern__ : Hybrid Page Object Model | 
| __Web Technology__ : PHP v.8.0x               | 
| __Scope of Testing__ : CSV Parser, Import CSV | 
| __Last Updated__ : 13-Aug-2024                | 
***
### Description Details:🥇
- code coverage percentage: ![coverage](https://img.shields.io/badge/coverage-99%25-yellowgreen)
- stable release version: ![version](https://img.shields.io/badge/version-1.0.0-blue)
- Last Updated: ![gem](https://img.shields.io/badge/Aug-2024-blue)
- status of third-party dependencies: ![dependencies](https://img.shields.io/badge/dependencies-requirements.txt-orange)
- [Uptime Framework](https://uptimerobot.com) percentage: ![uptime](https://img.shields.io/badge/uptime-100%25-brightgreen)
***
### How to clone project from Git Hub ?
* Open URL : git@github.ibm.com:classic-compute-qe/JiraAutomation.git
* Click on __https://github.ibm.com/classic-compute-qe__ JiraAutomation
* Click on __Code__
* Select __SSH__
* Click on __Copy__
* Open Terminal
* Navigate to the path where you want to clone the project Eg: cd /Users/deepaktogloor/Desktop
* Type ``` git clone git@github.ibm.com:classic-compute-qe/qe_ui_automation.git ```
***
### How to set up?
* Open Pycharm Editor
* Click on Open and select the project cloned
* Click on Terminal on the Pycharm Editor
* Click Green Arrow Mark to run query to activate __venv__ mode.
***
```commandline
cd venv/bin
```
```commandline
source activate
```
* Make sure you are into (venv) environment
* Copy the below command and run on terminal to install all packages from requirement.txt file
> pip install -r requirements.txt
---

* Copy and run the below command to see success message on terminal.
> python test_cases/test_file.py

***
* QE_UI_Automation_Hybrid_POM_Framework

""""""""""""""""""""""""""""""congratulations"""""""""""""""""""""""""""""\
********* S C H E M A T I C ********* F R A M E W O R K ********\
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\
********** S U C E S S F U L L Y |~~~~*~~~~| I N S T A L L E D ***********\
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
---
### Framework Structure
├──Schematic_JiraAutomation \
├── configuration \
│   └── config.ini \
├── CSV \
├── Documentation \
│   └── README.md \
├── excel \
├── Logs \
├── test_cases \
├── venv \
└── requirements.txt

---
# Configuration File - config.ini

This configuration file is used to specify paths, preferences, and logging information for the application.

## [files]
This section defines file paths for input and output.

```ini
[files]
rw_file_name = RHEL9.2
excel_input_path = excel/%(rw_file_name)s.xlsx
csv_output_path = CSV/%(rw_file_name)s.csv
```
> **rw_file_name** should always be passed only the filename **WITHOUT** extension.

- `rw_file_name`: The base name for files, used in constructing file paths.
- `excel_input_path`: The path to the Excel input file, dynamically constructed using rw_file_name.
- `csv_output_path`: The path to the CSV output file, also constructed using rw_file_name.

## [preference]
This section defines preferences for excluding certain sheets.

```ini
[preference]
exclude = no
exclude_sheets = TC_Ubuntu_24.04_Reload,TC_Ubuntu_24.04_Reclaim
```
- `exclude`: A flag to determine whether to exclude certain sheets. (no means sheets are not excluded).
- `exclude_sheets`: A comma-separated list of sheet names to exclude if exclude is set to yes.

## [logs]
This section defines the log file path.

```ini
[logs]
log_file_path = Logs
```
---
# Log Documentation

## Overview

This document provides a detailed breakdown of the log messages recorded on 2024-08-13. The log captures various levels of messages related to the processing of Excel sheets and the creation of a CSV file.

## Log Entries

### Debug Messages

- **2024-08-13 15:09:18,052** - `DEBUG` - Debug message
- **2024-08-13 15:09:18,075** - `DEBUG` - Found sheet names: ['TC_AddonWithR1Soft']

### Info Messages

- **2024-08-13 15:09:18,052** - `INFO` - Info message
- **2024-08-13 15:09:18,063** - `INFO` - Fetching Excel sheet names with prefix 'TC_'
- **2024-08-13 15:09:18,075** - `INFO` - Excluding sheets based on user preference
- **2024-08-13 15:09:18,090** - `INFO` - CSV created and saved to CSV/RHEL9.2.csv

### Warning Messages

- **2024-08-13 15:09:18,052** - `WARNING` - Warning message

### Error Messages

- **2024-08-13 15:09:18,052** - `ERROR` - Error message

### Critical Messages

- **2024-08-13 15:09:18,052** - `CRITICAL` - Critical message

## Summary

- The log begins with various messages of different levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
- Notably, it includes INFO-level messages detailing operations related to processing Excel sheets and generating a CSV file.
- The DEBUG messages provide additional context about the actions being performed, such as finding sheet names and user preferences.
- The final INFO message confirms the successful creation and saving of the CSV file.

## File Details

- **CSV File Created**: `CSV/RHEL9.2.csv`
- **Operation**: Conversion of selected Excel sheets to CSV format.

> **Note**: The file name 'RHEL9.2.csv' is just for a reference. The actual file name will be shown at the time of execution while the time you provide original file name to read as the excel file.

---
# Default Excel Path
> excel/RHEL9.2.xlsx

**NOTE** : Here RHEL9.2.xlsx file name is just a reference. Should be passed actual excel file name that you want to parse.

# Test Case Documentation

This document provides detailed information about a specific test case, including the assignee, the test plan, verification steps, and related metadata. The data is organized in a table format for clarity and easy reference.

## Test Case Details

The table below outlines the key aspects of the test case:

<table>
  <thead>
    <tr>
      <th style="background-color: yellow; color: red;">Assignee</th>
      <th style="background-color: yellow; color: red;">Summary</th>
      <th style="background-color: yellow; color: red;">Test Plan</th>
      <th style="background-color: yellow; color: red;">Verification</th>
      <th style="background-color: yellow; color: red;">QE Assignee</th>
      <th style="background-color: yellow; color: red;">Parent Id</th>
      <th style="background-color: yellow; color: red;">Labels</th>
      <th style="background-color: yellow; color: red;">Issue Type</th>
      <th style="background-color: yellow; color: red;">Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dtogloor</td>
      <td><strong>TC_00_Provision: with Intel Xeon 8474 and RHEL 9.2, R1 Soft Addon</strong></td>
      <td>
        <strong>Objective:</strong> Verify that RHEL 9.x with R1Soft Addon Provisioning process can be completed without errors.<br><br>
        <strong>Configuration:</strong><br>
        - <strong>SERVER</strong>: Intel Xeon 8474 Sapphire Rapids Processor, Core count 96, Features GPU, UEFI capable, 25GbE, NVMe, SGX<br>
        - <strong>RAM</strong>: 32GB / 256GB<br>
        - <strong>Hard Drive</strong>: NVMe primary drive and NVMe secondary storage (Any size)<br>
        - <strong>Chassis (Motherboard)</strong>: Lenovo<br>
        - <strong>Network Interface</strong>: Public and Private<br>
        - <strong>Port Speed</strong>: 25Gbps.<br>
        - <strong>OS Addon</strong>: R1Soft
      </td>
      <td>
        <strong>Steps to Verify:</strong><br>
        1. <strong>Configuration Verification:</strong> Log in to the server and check that all configurations are available as expected.<br>
        2. <strong>Addon Interface Verification:</strong> Ensure you can log into the web interface using the login details from the HWO.<br>
        3. <strong>License Verification:</strong> Confirm that the software has the correct license installed after logging into the addon web interface.
      </td>
      <td>dtogloor</td>
      <td>QEPVER-287</td>
      <td>IQE-Project-Testing</td>
      <td>Test Case</td>
      <td>Major</td>
    </tr>
  </tbody>
</table>

> For `Reload` & `Reclaim` Refer any previously created project test cases to get and understanding and Idea.

### Explanation of Table Columns
- **<span style="color: yellow;">**Assignee**</span>**: **Person responsible for executing the test case.**
- **<span style="color: yellow;">**Summary**</span>**: **A concise overview of the test case, including involved systems and software.**
- **<span style="color: yellow;">**Test Plan**</span>**: **Detailed steps and configurations needed for the test, including server specs and software addons.**
- **<span style="color: yellow;">**Verification**</span>**: **Detailed steps to ensure the test case passes, including configuration checks, web interface access, and license verification.**
- **<span style="color: yellow;">**QE Assignee**</span>**: **Quality Engineer assigned to oversee or review the test case.**
- **<span style="color: yellow;">**Parent Id**</span>**: **Identifier for the related parent task or feature.**
- **<span style="color: yellow;">**Labels**</span>**: **Tags used for categorizing or filtering the test case.**
- **<span style="color: yellow;">**Issue Type**</span>**: **The category of the task, such as "Test Case".**
- **<span style="color: yellow;">**Priority**</span>**: **Indicates the importance or urgency of the test case.**
---
# CSV file

## Default CSV Path
> csv/RHEL9.2.csv

| Assignee | Summary                                                            | Test Plan                                                                                                                                                                                                                                                                                                                                                                                                  | Verification                                                                                                                                                                                                 | QE Assignee | Parent Id  | Labels                | Issue Type | Priority |
|----------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|------------|-----------------------|------------|----------|
| dtogloor | TC_00_Provision : with Intel Xeon 8474 and RHEL 9.2, R1 Soft Addon | Verify that RHEL 9.x with R1Soft Addon Provisioning process can be completed without errors with below configuration<br>SERVER:  Intel Xeon 8474 Sapphire Rapids Processor, Core count 96, Features GPU, UEFI capable, 25GbE, NVMe, SGX<br>RAM: 32GB / 256GB<br>Hard Drive: NVMe primary drive and NVMe secondary storage (Any size)<br>Chassis(Motherboard) : Lenovo<br>NETWORK INTERFACE: Public and Private<br>PORT SPEED: 25Gbps.<br>Os Addon- R1Soft | 1) Login to server and check for all the configurations are available as expected.<br>2) For Addon, verify you can log into the web interface using the login details from the HWO<br>3) For Addon, verify the software has the correct license installed after login in the addon web interface. | dtogloor  | QEPVER-287 | IQE-Project-Testing | Test Case  | Major    |

> **Note** : The CSV file will be default placed in this CSV folder with Excel File name with extension .CSV (which is comma a seperated file)

---
# Test_cases

- **conftest.py** file is utilized for creating centralized fixtures and logs
- **test_csv_gen.py** file is an actual test file where backend options will be done and parse into csv file from excel and place it in default csv folder with filename.csv\
- **test_file.py** is the test file to ensure framework is properly configured and giving success message on the terminal.

---
```Requirements.txt```
---
- Is the file which contains all the libraries that are required to be perform and execute our test cases and test suite.
---

