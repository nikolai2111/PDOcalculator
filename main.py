def binary(num, length=8):
    return format(num, '#0{}b'.format(length + 2))


def hexadecimal(num, length=8):
    return format(num, '#0{}x'.format(length + 2))


def pdo_to_val(pdo):
    print("------------------------------------------------------------------------------")
    print(f"Values of the entered PDO:")
    print("------------------------------------------------------------------------------")
    pdo = binary(pdo, 32)
    print(f"Binary-Output:                              {pdo}")
    print(f"Current:                                    {int(pdo[-10:], 2) * 10} mA")
    print(f"Voltage:                                    {int(pdo[-20:-10], 2) * 50} mV")
    print(f"Reserved:                                   0b{pdo[-23:-20]}")
    print(f"Fast Role Swap not supported:               0b{pdo[-25:-23]}")
    print(f"Dual-role data supported:                   0b{pdo[-26:-25]}")
    print(f"USB communication capable not supported:    0b{pdo[-27:-26]}")
    print(f"Unconstrained power not available:          0b{pdo[-28:-27]}")
    print(f"Higher capability not supported:            0b{pdo[-29:-28]}")
    print(f"Dual-role power not supported:              0b{pdo[-30:-29]}")
    print(f"Fixed Supply:                               0b{pdo[-32:-30]}")


def val_to_pdo(current,
               voltage,
               frs_n_supported,
               drd_supported,
               usbcomm_n_supported,
               ext_power_n_available,
               highercapab_n_supported,
               drp_n_supported,
               type_fixed):
    print("------------------------------------------------------------------------------")
    print(f"PDO of the entered Values:")
    print("------------------------------------------------------------------------------")
    print(
        f"Hex-Output: {hexadecimal(int(binary(type_fixed, 2)[-2:] + binary(drp_n_supported, 1)[-1:] + binary(highercapab_n_supported, 1)[-1:] + binary(ext_power_n_available, 1)[-1:] + binary(usbcomm_n_supported, 1)[-1:] + binary(drd_supported, 1)[-1:] + binary(frs_n_supported, 2)[-2:] + binary(0, 3)[-3:] + binary(voltage // 50, 10)[-10:] + binary(current // 10, 10)[-10:], 2))}")


if __name__ == '__main__':
    pdo_to_val(0x2019096)
    val_to_pdo(1500, 5000, 0, 1, 0, 0, 0, 0, 0)
