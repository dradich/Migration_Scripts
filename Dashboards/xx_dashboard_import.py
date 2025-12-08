from arcgis.gis import GIS
import pandas as pd
import warnings,urllib3,time,json,csv,os
from arcgis.apps.dashboard import Dashboard

warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
target = GIS("*target url*", "*target UN*", "*target pw*")
output_json=r"*path to folder containg json files*"
table = pd.read_csv(r"*Path to CSV inventory from Dev*")
for filename in os.listdir(output_json):
    file_item_id=filename.split(".")[0]
    full_path=os.path.join(output_json, filename)
    for index, row in table.iterrows():
        df_item_id=row['Item ID']
        if file_item_id == df_item_id:
            title=row['Title']
            print(f"Creating Dashboard - {title}")
            dashboard = Dashboard()
            dashboard_item = dashboard.save(title, overwrite=True)
            with open(full_path, 'r', encoding='utf-8') as json_file:
                dash_data = json.load(json_file)
            dashboard_item.update(data=dash_data)
            print(f"  - Dashboard '{title}' updated to match source.")
