#!/usr/bin/env/python
def init():
    global mutant_genes
    mutant_genes = """{
  variant_report{
    delins_variants{
      gene
    }
    indel_variants{
      gene
    }
    snv_variants{
      gene
    }
    gene_fusion_variants{
      gene1
      gene2
    }
    copy_number_variants{
      gene
    }
  }
}"""
