BROKEN = 'BKN'
OVERCAST = 'OVC'

def findMinimumCeiling(report):
    if report.iter('sky_condition') is None:
        return None

    ceiling = None
    for skyCondition in report.iter('sky_condition'):
        layer = skyCondition.attrib
        coverage = layer['sky_cover']
        if coverage not in [BROKEN, OVERCAST]:
            continue
        base = int(layer['cloud_base_ft_agl']) if 'cloud_base_ft_agl' in layer else 0
        if (ceiling is None) or (base < ceiling):
            ceiling = base
    return ceiling
