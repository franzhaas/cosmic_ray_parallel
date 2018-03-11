*** settings ***
Library         Process
Library         OperatingSystem
Library         Collections
Library         create_report
*** Test cases ***
acceptance
      Run Process          cosmic-ray            exec            test/session_parallel
      Run Process          cosmic-ray            exec            test/session_local
      ${res_local}=        create_report         test/session_local.json
      ${res_parallel}=     create_report         test/session_parallel.json
      Should be equal      ${res_parallel}       ${res_local}
