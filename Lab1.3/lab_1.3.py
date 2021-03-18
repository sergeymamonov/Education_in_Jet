from pysnmp.hlapi import *


def print_result(results):
    for result in results:
        error_indication, error_status, error_index, var_binds = result
        if error_indication:
            print(error_indication)
        elif error_status:
            print(f"{error_status.prettyPrint()} at {error_index and var_binds[int(error_index) - 1][0] or '?'}")
        else:
            for varBind in var_binds:
                print(varBind)
                print(' = '.join(x.prettyPrint() for x in varBind))


results_get = getCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)),
                     ContextData(), ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)))
print_result(results_get)

results_next = nextCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)),
                       ContextData(), ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.2")), lexicographicMode=False)
print_result(results_next)
