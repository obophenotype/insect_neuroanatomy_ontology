from owltools.graph import OWLGraphWrapper
from owl2pdm_tools import ont_manager
import warnings
#from tsv2pdm import rcd

import requests
r = requests.get('https://insectbraindb.org/api/v1/brain_region/')
ibd_neuropils = r.json()
import re

# Each term in first level of list is a block.  Make this part of adult brain (UBERON_6003624)
# heirarchy underneath = partonomy - single inheritance.
# Need to merge left and right (do this on short hand)
# So can make table
# ibdb_id | ibd_name | ibdb_abbv | uberon term name (TBA) | part_of | BrainName ABBV| FBbt term
print "\t".join(['ibdb_id', 'ibdb_name', 'ibdb_abbv', 
                'Uberon_label', 'part_of', 'BrainName_abbv',
                'FBbt_id', 'FBbt_name'])


def name_gen(n):
    """Generates Uberon term name by matching up to '-' 
    stripping remaining trailing space
    converting to lower case"""
    U_name_m = re.match('(.+)-', n)
    if U_name_m:
        return U_name_m.group(1).strip().lower()
    else:
        return n.lower()
    
def abbv_gen(a):
    m = re.match('(.+)-(l|r)', a)
    if m:
        return m.group(1)
    else:
        return a

class row_gen():
    def __init__(self, ont_path):
        self.om = ont_manager(file_path=ont_path)
        self.lookup = self.gen_lookup()
    
    def gen_lookup(self):
        cs = self.om.ont.getClassesInSignature()
        BrainName_syns = {}
        BrainName_FBbt_lookup = {}
        
        for c in cs:
            sf = self.om.bi_sfp.getShortForm(c)
            subs = self.om.get_subsets(owl_entity_sfid = sf)
            if 'BrainName' in subs:
                syns = self.om.get_annotations(owl_entity_sfid = sf,
                                                        owl_annotation_property_sfid = 'hasExactSynonym')
                BrainName_syns[sf] = syns
                for s in syns:
                    if s not in BrainName_FBbt_lookup:
                        BrainName_FBbt_lookup[s] = []
                    BrainName_FBbt_lookup[s].append(sf)
        return BrainName_FBbt_lookup

    def print_row(self, j, superpart_name):
        ID = str(j['id'])
        uname = name_gen(j['name'])
        u_abbv = abbv_gen(j['abbreviation'])
        FBbt = ''
        FBbt_label = ''
        if u_abbv in self.lookup.keys():
            if len(self.lookup[u_abbv]) == 1:
                FBbt = self.lookup[u_abbv][0]
                FBbt_label = self.om.get_labels(FBbt)[0]
            else:
                warnings.warn('%s %s has multiple matches: %s' % (uname, u_abbv, (str(self.lookup[u_abbv]))))
        print "\t".join([ID, j['name'], j['abbreviation'], uname, superpart_name, 
                         u_abbv, FBbt, FBbt_label])        
        return uname


rg = row_gen('/repos/drosophila-anatomy-developmental-ontology/fbbt/releases/fbbt-simple.owl')
 
r = requests.get('https://insectbraindb.org/api/v1/brain_region/')
ibd_neuropils = r.json()            

for b in ibd_neuropils:
    nbu = rg.print_row(j = b, superpart_name='adult brain')
    for n in b['neuropils']:
        nu = rg.print_row(j = n, superpart_name=nbu)
        for ns in n['subregions']:
            rg.print_row(j = ns, superpart_name=nu)

                    
         
