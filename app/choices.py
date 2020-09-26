class MachineIncidentChoices:
    machine_choices = (
        ("CHPP Fix Plant", "CHPP Fix Plant"),
        ("PORT Fix Plant", "PORT Fix Plant")
    )

    shutdown_type = (
        ("fully_shutdown", "Fully Shutdown"),
        ("running_with_fail", "Running with Fail")
    )

    shutdown_area = (
        ("genset_power", "Genset/Power"),
        ("mcc", "MCC"),
        ("feeder", "Feeder"),
        ("breaker", "Breaker"),
        ("cv910", "CV910"),
        ("sizer", "Sizer"),
        ("cv911", "CV911"),
        ("scada_plc", "SCADA & PLC"),
        ("sampler_system", "Sampler System"),
        ("iron_trap", "Iron Trap"),
        ("metal_detector", "Metal Detector"),
        ("belt_scale", "Belt Scale")
    )