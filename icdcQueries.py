#!/usr/bin/env python

def init():
    global all_types
    all_types = """{
          __schema{
            types{
              name
              kind
              description
            }
          }
        }"""

    global all_queries
    all_queries = """{
      __schema{
        queryType{
          fields{
            name
            description
          }
        }
      }
    }"""

    global sbg_single_case
    sbg_single_case = """{
      case(case_id: "NCATS01CCB030162"){
        case_id
        cohort{
          cohort_description
          cohort_dose
          study_arm{
            arm
            study{
              clinical_study_designation
              clinical_study_name
            }
          }
        }
        demographic{
          breed
          weight
          sex
          neutered_indicator
          patient_age_at_enrollment
        }
        diagnoses{
          disease_term
          stage_of_disease
          primary_disease_site
          concurrent_disease
          concurrent_disease_type
        }
        visits{
          visit_date
          visit_number
          physical_exams{
            day_in_cycle
          }
        }
        samples{
          sample_id
          sample_type
          general_sample_pathology
          date_of_sample_collection
          necropsy_sample
          percentage_tumor
          percentage_stroma
          comment
          files{
            file_name
            file_type
            file_description
            file_format
            file_size
            md5sum
            file_locations
            uuid
          }
        }
      }
    }"""
