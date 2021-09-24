INSERT INTO rdata (a,b,x) VALUES
('wrong','row',-100);
select * from rdata;

INSERT INTO rdata (a,b,x) VALUES
('right','row',100);
select * from rdata;