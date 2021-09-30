ALTER TABLE player_bios
ADD COLUMN new_height numeric;
			 
UPDATE player_bios
set new_height = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN new_height TO height;
			 
SELECT firstname,lastname,height FROM player_bios limit 5;	