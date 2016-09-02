
# coding: utf-8

# In[35]:

import requests
r = requests.get('https://insectbraindb.org/api/v1/brain_region/')
ibd_neuropils = r.json()
import re
# Each term in first level of list is a block.  Make this part of adult brain (UBERON_6003624)
# heirarchy underneath = partonomy - single inheritance.
# Need to merge left and right (do this on short hand)
# So can make table
# ibdb_id | ibd_name | ibdb_abbv | uberon term name (TBA) | part_of | BrainName ABBV| FBbt term
print("ibdb_id\tibd_name\tibdb_abbv\tuberon term name (TBA)\tpart_of\tBrainName ABBV\tFBbt term")

def name_gen(n):
    """Generates Uberon term name by matching up to '-' 
    stripping remaining trailing space
    converting to lower case"""
    U_name_m = re.match('(.+)-', n)
    if U_name_m:
        return U_name_m.group(1).strip().lower()
    else:
        return n
    
def abbv_gen(a):
    m = re.match('(.+)-(l|r)', a)
    if m:
        return m.group(1)
    else:
        return a
    
def print_row(j, superpart_name):
    ID = str(j['id'])
    uname = name_gen(j['name'])
    u_abbv = abbv_gen(j['abbreviation'])
    print ("\t".join([ID, j['name'], j['abbreviation'], uname, superpart_name, u_abbv]))
    return uname


for b in ibd_neuropils:
    nbu = print_row(b, 'adult brain')
    for n in b['neuropils']:
        nu = print_row(n, nbu)
        for ns in n['subregions']:
            print_row(n, nu)

    


# In[ ]:




# In[ ]:



