from Demos.walmartScraper import Walmart
import json

# Get deals
extracted_records = Walmart().get_deals('TV')

# Save results to a json file
with open('products.json', 'w') as outfile:
    json.dump(extracted_records, outfile, indent=4)
