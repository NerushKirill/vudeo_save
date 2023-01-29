
/*
CREATE TABLE subdivision (
  [subdivision_id] INTEGER NOT NULL PRIMARY KEY,
  [es_or_buro] CHAR(30),
  [number_division] INTEGER(2),
  [supervisor] VARCHAR(90),
  [cabinet_mse] CHAR(10),
  [cam_flow] CHAR(10),
  [download_link] VARCHAR(255)
  );

CREATE TABLE IF NOT EXISTS note (
  [note_id] INTEGER NOT NULL PRIMARY KEY,
  [count_record_day] INTEGER,
  [time_start_mse_day] TIME,
  [time_end_mse_day] TIME,
  [gave] CHAR(90)
  );

CREATE TABLE IF NOT EXISTS mse (
  [record_id] INTEGER NOT NULL PRIMARY KEY,
  [id_es_buro] INTEGER references subdivision(subdivision_id),
  [note_id] INTEGER references note(note_id),
  [s_name] VARCHAR(30),
  [f_name] VARCHAR(30),
  [m_name] VARCHAR(30),
  [birthday] DATE,
  [date_mse] DATE,
  [time_start_mse] TIME,
  [time_end_mse] TIME,
  [gave] VARCHAR(90)
  );
*/

INSERT INTO subdivision
VALUES (
  1,
  'Экспертный состав',
  1,
  'Степанова Р.Р.',
  '223, 205',
  'D1, D2',
  'http://hickvision.ru'
  );


select * from subdivision;


