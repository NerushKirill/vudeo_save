-- from mysql db_test

CREATE TABLE IF NOT EXISTS note (
  note_id INTEGER NOT NULL PRIMARY KEY,
  iso_number VARCHAR(10),
  count_record_day INTEGER(2),
  time_start_mse_day TIME,
  time_end_mse_day TIME,
  gave CHAR(90)
  );

CREATE TABLE IF NOT EXISTS mse (
  record_id INTEGER NOT NULL PRIMARY KEY,
  note_id INTEGER references note(note_id),
  s_name VARCHAR(30),
  f_name VARCHAR(30),
  m_name VARCHAR(30),
  birthday DATE,
  date_mse DATE,
  time_start_mse TIME,
  time_end_mse TIME
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


INSERT INTO mse
VALUES (
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

/*
select
  concat(s_name, ' ', left(f_name, 1), '.', LEFT(m_name, 1), '.') as 'out'
from
  mse;
*/