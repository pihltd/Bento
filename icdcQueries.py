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
      case(case_id:NCATS01CCB030162'){
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

    global sbg_all_cases
    sbg_all_cases = """{
      case{
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

#https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad
    global prod_sbg_single_case
    prod_sbg_single_case = ''' query($case: String!) {
      case(case_id: $case){
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
          visit_date'
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
    } '''

    global demo_query
    demo_query = '''{
  case{
    case_id
    cohort{
      cohort_description
      cohort_dose
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
    }
    samples{
      sample_id
      physical_sample_type
      general_sample_pathology
      date_of_sample_collection
      necropsy_sample
      percentage_tumor
      percentage_stroma
      comment
    }
  }
}'''

    global table_demo
    table_demo = '''{
case{
  case_id
  demographic{
    breed
    weight
    sex
    patient_age_at_enrollment
  }
 }
}'''
