CREATE TABLE nguyendinhchieu(
	"mshs"	INTEGER,
	"truong_cu"	TEXT,
	"nv1"	INTEGER,
	"nv2"	INTEGER,
	"tong_diem"	FLOAT
);

SELECT * FROM lythaito ORDER BY diem_trinhhoaiduc DESC LIMIT 450;

INSERT INTO diem_binhphu SELECT * FROM binhphu ORDER BY tong_diem DESC;
