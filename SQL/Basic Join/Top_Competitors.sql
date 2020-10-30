SELECT h.hacker_id, h.name
    FROM hackers as h
    JOIN (submissions as s, challenges as c, difficulty as d)
        ON (
            s.hacker_id = h.hacker_id
            AND s.challenge_id = c.challenge_id
            AND c.difficulty_level = d.difficulty_level
           )
    WHERE s.score = d.score
    GROUP BY h.hacker_id, h.name
        HAVING COUNT(*) > 1
    ORDER BY COUNT(*) DESC, h.hacker_id
