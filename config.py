# CURRENT_URL = 'https://www.basketball-reference.com/leagues/NBA_2024_standings.html'
# PROJECTION_URL = 'https://www.basketball-reference.com/friv/playoff_prob.html'

# WESTERN_CONFERENCE_ID = "div_confs_standings_W"
# EASTERN_CONFERENCE_ID = "div_confs_standings_E"

# WESTERN_PROJECTIONS_ID = "all_projected_standings_w"
# EASTERN_PROJECTIONS_ID = "all_projected_standings_e"

RUN_DICT = {
    'current' : {
        'western'  : "div_confs_standings_W"
        ,'eastern' : "div_confs_standings_E"
        ,'url'     : 'https://www.basketball-reference.com/leagues/NBA_2024_standings.html'}

    ,'projection' : {
        'western'  : "all_projected_standings_w"
        ,'eastern' : "all_projected_standings_e"
        ,'url'     : 'https://www.basketball-reference.com/friv/playoff_prob.html'}
}

RUN_TYPES = RUN_DICT.keys()