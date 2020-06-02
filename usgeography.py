# all raw data in .txt files taken from jetpunk.com

def stateToCounties(filename):
    """
    :param filename: text containing state name, tab, county name, enter button...
    :return: { state name : [list of counties in that state] }
    """

    filein = open(filename, 'r')
    lines = filein.readlines()
    rawdata = []
    states = {}

    for line in lines:
        line = line.strip('\n').split('\t')
        rawdata += [line]

    filein.close()

    for part in rawdata:
        if part[0] not in states.keys():
            states[part[0]] = [part[1]]
        else:
            states[part[0]] += [part[1]]
    return states


stc = stateToCounties('uscounties.txt')


# save the results into a variable

def numCounties(dict):
    """
    :param dict: use the previous function as your parameter
    :return: { state name : no. of counties in state } - { AL : 67 }
    """

    number = {}

    for state, counties in dict.items():
        number[state] = len(counties)
    return number


# print(numCounties(stc))

def countyCount(dict, county_name='None'):
    """
    :param dict: takes in { state name : [list of counties] }
    :param county_name: will tell you how many counties in the US have that particular name
    :return: all counties of the US and how often they occur OR
            something like 'There are 26 counties in the US called Jefferson.'
    """
    try:
        common_county = {}
        all_counties = []

        for counties in dict.values():
            for county in counties:
                all_counties += [county]
        all_counties.sort()

        for county in all_counties:
            if county not in common_county.keys():
                common_county[county] = all_counties.count(county)

        if county_name == 'None':
            return common_county
        else:
            county_name = county_name.split(' ')
            words = [i.capitalize() for i in county_name]
            actual = ' '.join(words)
            return 'There are ' + str(common_county[actual]) + ' counties in the US called ' + str(actual) + '.'
    except:
        return 'There is no county called ' + str(actual) + '.'


def countyToState(filename, county='None'):
    """
    :param filename: takes in a file of state name, tab, county name, enter button...
    :param county: optional parameter
    :return: { county name : [State 1, State 2, ...] } if county NOT specified
             OR [State 1, State 2, ...] if county specified
            Example: ['AL', 'AR', 'CO', ...] if 'Jefferson' is specified
    """
    try:
        filein = open(filename, 'r')
        lines = filein.readlines()
        raw_data = []
        counties = {}
        for line in lines:
            line = line.strip('\n').split('\t')
            raw_data += [line]
        for part in raw_data:
            if part[1] not in counties.keys():
                counties[part[1]] = [part[0]]
            else:
                counties[part[1]] += [part[0]]
        if county != 'None':
            return counties[county]
        return counties
    except:
        return str(county) + ' is not a county in the US.'


cts = countyToState('uscounties.txt')


def stateToCapital(filename, state='None'):
    """
    :param filename: file containing state, tab, capital
    :return: {state : capital} for all 50 states OR something like
            'The capital of New Jersey is Trenton.' if the second parameter is filled
    """
    try:
        filein = open(filename, 'r')
        lines = filein.readlines()
        capitals = {}
        for line in lines:
            line = line.strip('\n').split('\t')
            capitals[line[0]] = line[1]
        filein.close()
        if state != 'None':
            state = state.split(' ')
            words = [i.capitalize() for i in state]
            actual = ' '.join(words)
            # check against someone not using proper capitalisation
            return 'The capital of ' + str(actual) + ' is ' + str(capitals[actual]) + '.'
        return capitals
    except:
        return str(actual) + ' is not a US state.'
