-- SQL script that creates an index idx_name_first_score on names with first letter and score
-- Only the first letter of name AND score must be indexed

CREATE INDEX idx_name_first_score ON names (name(1), score);