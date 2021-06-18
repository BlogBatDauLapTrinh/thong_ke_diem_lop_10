CREATE TABLE diem_trinhhoaiduc (
	"mshs"	INTEGER,
	"truong_cu"	TEXT,
	"nv1"	INTEGER,
	"nv2"	INTEGER,
	"tong_diem"	FLOAT
);

SELECT * FROM trinhhoaiduc ORDER BY diem_trinhhoaiduc DESC LIMIT 450;

INSERT INTO diem_trinhhoaiduc SELECT * FROM trinhhoaiduc ORDER BY tong_diem DESC
