# insect neuroanatomy ontology

![Megalopta](http://insectbraindb.org/static/images/Megalopta_frontal.png)
Meglopta genalis BCI Panama (Photo credit Ajay Narendra) - pic hosted by [Insect Brain Database](http://insectbraindb.org/)

## Aims & use cases

The main aim of this project is to provide a simple integration layer to allow cross linking of online insect brain resources such as the [Insect Brain Database](http://insectbraindb.org/)(IBDB) and [Virtual Fly Brain](www.virtualflybrain.org)(VFB). It could also provide a way to cross-search these resources - for example, it should be possible to cross search VFB and the IBDB to find neurons connecting any two sepecified neuropils.

## Introduction

In 2014, Ito _et al._ published [A systematic nomenclature for the insect brain](http://www.ncbi.nlm.nih.gov/pubmed/24559671). This potentially provides the basis for a standard ontology of insect brain anatomy, commonly referred to as the BrainName nomenclature.  It has been used as the basis of the IBDB - providing a framework for integrative searches across species.  It has also been used to structure the representation of brain anatomy in the [Drosophila neuroanatomy ontology](https://github.com/FlyBase/drosophila-anatomy-developmental-ontology) used by [Virtual Fly Brain](www.virtualflybrain.org)(VFB).  VFB and IBDB also include 3D insect brains painted according to this standard.

## Plan for integration:

1. IBDB provides an rest API. It should be possible to use this to dump a JSON respresenation of BrainName terms.  
1. Generate unique Insect neuroanatomy ontoogy (INO?) terms with IDs, basic (CARO) classification, part & innervates relationships.
1. Generate OWL file that maps up from DAO to INO classes.

# Usage: 
