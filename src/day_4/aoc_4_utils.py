import re


def read_data_from_txt(filename) -> list:
    try:
        with open(filename) as f:
            data_list = []
            for data in f.read().split("\n\n"):
                data_list.append({dict[0]: dict[1]
                                  for dict in re.findall(r'(\w+):(\S+)', data)})
            return data_list
    except OSError as identifier:
        return []


def is_valid_simple(passport, required) -> bool:
    return not any(required - passport.keys())


def is_valid_adv(passport, required) -> bool:
    try:
        if is_valid_simple(passport, required):
            byr = int(passport["byr"])
            if not 1920 <= byr <= 2002:
                return False
            iyr = int(passport["iyr"])
            if not 2010 <= iyr <= 2020:
                return False
            eyr = int(passport["eyr"])
            if not 2020 <= eyr <= 2030:
                return False
            hgt = passport["hgt"]
            hgt_unit = str(hgt[-2:])
            hgt_value = int(hgt[:-2])
            if hgt_unit != "in" and hgt_unit != "cm":
                return False
            if hgt_unit == "cm" and not 150 <= hgt_value <= 193:
                return False
            if hgt_unit == "in" and not 59 <= hgt_value <= 76:
                return False
            hcl = passport["hcl"]
            if hcl[0] != "#" or len(hcl) != 7:
                return False
            int(hcl[1:], 16)
            ecl = passport["ecl"]
            if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                return False
            pid = passport["pid"]
            if not pid.isdigit() or len(pid) != 9:
                return False
            return True
    except:
        return False
