#  Mapping files:

## Synaptic neuropil mappings

Background: Both FBbt and IBDB have neuropils with names, abbreviations and partonomy based on: Ito, K., Shinomiya, K., Ito, M., Armstrong, J. D., Boyan, G., Hartenstein, V., … Vosshall, L. B. (2014). A systematic nomenclature for the insect brain. Neuron, 81(4), 755–65. doi:10.1016/j.neuron.2013.12.017

We aim to map these to general classes to live in Uberon.  All classes should have PMID:24559671 as a reference. 


file: IBDB_neuropils_2_Uberon_FBbt.tsv

* **Columns**: 
  * *ibdb_id*:  ID number in IBDB JSON
  * *ibdb_name*: Name in IBDB JSON
  * *ibdb_abbv*: Abbreviation in IBDB JSON
  * *Uberon_label*:  label for proposed Uberon term. 
    * Derived from idbdb_name by stripping terminal ' - (l/r)' where present and converting to lower-case.
  * *part_of*: part_of parent for proposed Uberon term
    * Derived from the JSON hierarchy.  Uses the same names as in Uberon label.
  * *BrainName_abbv*: Abbreviation for proposed Uberon term
    * Derived from idbdb_name by stripping terminal ' - (l/r)'
  * *FBbt_id*: ID of 'equivalent' class in FBbt
    * Mapped automatically by searching for classes in SubSet:BrainName and then matching Uberon ABBV to synonyms. Some additional manual mapping was done based on Ito et al., 2014
  * *FBbt_name*: Name of 'equivalent' class in FBbt
    * Pulled from FBbt
  
Generation:  This file was mostly generated progamatically using JSON from https://insectbraindb.org/api/v1/brain_region/
& [fbbt-simple.owl](http://purl.obolibrary.org/obo/fbbt/fbbt-simple.owl).

