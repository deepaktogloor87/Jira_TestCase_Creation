
def test_excel_sheet_names_with_prefix(get_the_excel_sheet_names_with_prefix,
                                       exclude_sheets_,
                                       create_csv_from_sheets):
    # Simulate the data returned by fixtures
    sheet_names = get_the_excel_sheet_names_with_prefix
    print('Sheet names with prefix TC_:', sheet_names)

    excluded_sheets = exclude_sheets_
    print("Sheets are excluded provided by the user:", excluded_sheets)

    # Simulate the creation of CSV file
    csv_path = create_csv_from_sheets
    print("CSV file created successfully under the path:", csv_path)

    # Assertions or further testing logic can be added here
    # assert csv_path == config["files"]["csv_output_path"]  # Adjust this based on your actual setup
