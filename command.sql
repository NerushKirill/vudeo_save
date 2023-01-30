
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
  [iso_number] VARCHAR(10),
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
  [time_end_mse] TIME
  );

*/

/*
PRAGMA TABLE_INFO(subdivision);
PRAGMA TABLE_INFO(note);
PRAGMA TABLE_INFO(mse);
*/

INSERT INTO subdivision
VALUES (
  1,
  'Экспертный состав',
  1,
  'Фамилия И.О.',
  '223, 205',
  'D1, D2',
  'http://hickvision.ru'
  );


INSERT INTO note
VALUES (
  1,
  '244/ВН',
  2,
  '9:30',
  '12:00',
  'Сдал ФИО'
  );


--mse1
INSERT INTO mse
VALUES (
  1,
  1,
  1,
  'Фамилия',
  'Имя',
  'Отчество',
  '01.01.1900',
  '02.02.2000',
  '9:30',
  '11.00'
  );

--mse 2
INSERT INTO mse
VALUES (
  2,
  1,
  1,
  'Фамилия2',
  'Имя2',
  'Отчество2',
  '03.03.1900',
  '04.04.2004',
  '11:00',
  '12.00'
  );
