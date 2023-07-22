-- Script that creates an index on only the first letter of a name
CREATE INDEX idx_name_first ON names ( name(1) );