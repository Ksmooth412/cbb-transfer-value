-- One named view across all seasons
CREATE OR REPLACE VIEW players AS
SELECT "32" AS player_id, "0" AS player, "1" AS team, "2" AS conf,
       "31" AS season, "25" AS class_yr, "64" AS role,
       "3" AS games, "4" AS min_pct, "5" AS ortg, "6" AS usage
FROM raw_players;

-- Each player's season next to his previous season
CREATE OR REPLACE VIEW transfers AS
WITH paired AS (
    SELECT *,
        LAG(team)    OVER w AS prev_team,
        LAG(conf)    OVER w AS prev_conf,
        LAG(season)  OVER w AS prev_season,
        LAG(min_pct) OVER w AS prev_min_pct,
        LAG(ortg)    OVER w AS prev_ortg,
        LAG(usage)   OVER w AS prev_usage
    FROM players
    WINDOW w AS (PARTITION BY player_id ORDER BY season)
)
SELECT * FROM paired
WHERE prev_team IS NOT NULL
  AND team <> prev_team
  AND season = prev_season + 1;
