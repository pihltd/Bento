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
    global diseases
    diseases = """
        {
          case{
            case_id
            ctep_category
          }
        }
    """
    global patients
    patients = """
    {
    case{
      ethnicity
      race
      gender
      prior_drugs
      }
    }
    """

    global mutant_patients
    mutant_patients = """
        {
            case{
                case_id
                specimens{
                    assignment_reports{
                        variant_report{
                            gene_fusion_variants{
                                gene1
                                gene2
                            }
                            delins_variants{
                                gene
                            }
                            copy_number_variants{
                                gene
                            }
                            snv_variants{
                                gene
                            }
                            indel_variants{
                                gene
                            }
                        }
                    }
                }
            }
        }
    """
