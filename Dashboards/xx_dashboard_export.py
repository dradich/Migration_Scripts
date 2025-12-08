from arcgis.gis import GIS
import pandas as pd
import warnings,urllib3,time,json,csv
warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
source = GIS("*source url*", "*source UN*", "*source pw*")

table = pd.read_csv(r"*Path to CSV inventory from Dev*")
output_json=r"*path to folder that json files will be written to*"
for index, row in table.iterrows():
    item_id=row['Item ID']
    title=row['Title']
    item_type=row['Item Type']
    if item_type == "Dashboard":
        print(f"Processing Item: {title} (ID: {item_id}, Type: {item_type})")
        source_item=source.content.get(item_id)
        dash_json=source_item.get_data()
        with open(f"{output_json}\\{item_id}.json", 'w', encoding='utf-8') as json_file:
            json.dump(dash_json, json_file, ensure_ascii=False, indent=4)

