CREATE OR REPLACE VIEW transfer_features AS
SELECT *,
    CASE WHEN prev_conf IN ('ACC','B10','B12','SEC','BE','P12') THEN 2 ELSE 1 END AS prev_level,
    CASE WHEN conf      IN ('ACC','B10','B12','SEC','BE','P12') THEN 2 ELSE 1 END AS new_level,
    (CASE WHEN conf      IN ('ACC','B10','B12','SEC','BE','P12') THEN 2 ELSE 1 END)
  - (CASE WHEN prev_conf IN ('ACC','B10','B12','SEC','BE','P12') THEN 2 ELSE 1 END) AS level_jump,
    ortg - prev_ortg AS ortg_change
FROM transfers
WHERE prev_min_pct >= 20 AND min_pct >= 20;
