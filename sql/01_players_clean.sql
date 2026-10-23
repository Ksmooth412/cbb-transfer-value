-- Clean, named view of Torvik player stats
CREATE OR REPLACE VIEW players_2025 AS
SELECT
    "32"  AS player_id,
    "0"   AS player,
    "1"   AS team,
    "2"   AS conf,
    "31"  AS season,
    "25"  AS class_yr,
    "26"  AS height,
    "64"  AS role,
    "3"   AS games,
    "4"   AS min_pct,
    "5"   AS ortg,
    "6"   AS usage,
    "7"   AS efg_pct,
    "8"   AS ts_pct,
    "9"   AS orb_pct,
    "10"  AS drb_pct,
    "11"  AS ast_pct,
    "12"  AS to_pct,
    "15"  AS ft_pct,
    "18"  AS two_pct,
    "20"  AS three_att,
    "21"  AS three_pct,
    "22"  AS blk_pct,
    "23"  AS stl_pct
FROM raw_players_2025;
