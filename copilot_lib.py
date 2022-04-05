from google.cloud import bigquery
import pandas as pd

def from_bigquery(query:str, project='sixty-odp-xaxis-prod', location='EU'):
    client = bigquery.Client(location=location, project=project)
    query_job = client.query(
        query,
        # Location must match that of the dataset(s) referenced in the query.
        location=location,
    )  # API request - starts the query
    results = query_job.result()
    return client.query(query).to_dataframe(create_bqstorage_client=False)



class BonsaiTree(object):
    def __init__(self):
        pass
    
    def from_ip_df(self, df):
        pass
    
    def from_decisiontree(self, model):
        pass      


''' Like this        
model = DecisionTreeRegressor()
modelf.fit(X, y)
                 
bt = BonsaiTree().from_decisiontree(model)
bt = BonsaiTree().from_iplist(ip_list)
bt = BonsaiTree()

for land in bundeslaender:
    bt.add_node(land)
    for zeit in zeitraueme:
        bt.add_node(zeit)

bt.push_to_lineitem(blabla)
bt.push_to_xandr(lineitem=blabla)
bt.push_to_aa(lineitem=blabla)
                 
                 
bt = BonsaiTree().from_ip_df(ip_df)
                 
bt.push_to_csv(filename)


Active Agent example:

[11:30] Alicia Schuller

infos = """{
"code": "( cluster('State_NRW') AND cluster('Time_NRW') ) OR ( cluster('State_Hessen') AND cluster('Time_Hessen') )
OR ( cluster('State_Bayern') AND cluster('Time_Bayern') ) OR ( cluster('State_Berlin') AND cluster('Time_Berlin') )
OR ( cluster('State_Bremen') AND cluster('Time_Bremen') ) OR ( cluster('State_Hamburg') AND cluster('Time_Hamburg') )
OR ( cluster('State_Sachsen') AND cluster('Time_Sachsen') ) OR ( cluster('State_Sachen-Anhalt') AND cluster('Time_Sachsen-Anhalt') )
OR ( cluster('State_Mecklenburg-Vorpommern') AND cluster('Time_Mecklenburg-Vorpommern') ) OR ( cluster('State_Brandenburg') AND cluster('Time_Brandenburg') )
OR ( cluster('State_Niedersachsen') AND cluster('Time_Niedersachsen') ) OR ( cluster('State_Thueringen') AND cluster('Time_Thueringen') )
OR ( cluster('State_Saarland') AND cluster('Time_Saarland') ) OR ( cluster('State_Rheinland-Pfalz') AND cluster('Time_Rheinland-Pfalz') )
OR ( cluster('State_Schleswig-Holzstein') AND cluster('Time_Schleswig-Holstein') ) OR ( cluster('State_Baden-Wuerttemberg') AND cluster('Time_Baden-Wuerttemberg') )" }
"""

'''    
