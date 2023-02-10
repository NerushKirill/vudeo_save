-- from mysql db_test

/* services
DROP DATABASE video_saver;
*/

CREATE DATABASE video_saver;

USE video_saver;

/* services
DROP TABLE subdivision;
*/

CREATE TABLE IF NOT EXISTS subdivision (
  subdivision_id INTEGER NOT NULL PRIMARY KEY,
  es_or_buro CHAR(30),
  number_division INTEGER(2),
  supervisor VARCHAR(90),
  cabinet_mse CHAR(10),
  cam_flow CHAR(10),
  download_link VARCHAR(255)
  );


# Replenishment of the table "subdivision"
/*
LOAD DATA INFILE 'c:/filling.csv' 
INTO TABLE subdivision
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

DELETE FROM subdivision WHERE (subdivision_id = '') OR (subdivision_id IS NULL);
*/

SELECT * FROM subdivision;


/* services
DROP TABLE note;
TRUNCATE TABLE note;
*/

CREATE TABLE IF NOT EXISTS note (
  note_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  iso_number VARCHAR(20),
  count_record_day INTEGER(2),
  date_mse DATE,
  time_start_mse_day TIME,
  time_end_mse_day TIME,
  current_date_note DATETIME,
  gave CHAR(90)
  );

/* example
INSERT INTO note (iso_number, count_record_day, date_mse, time_start_mse_day, time_end_mse_day, current_date_note, gave)
VALUES ('003/ВН', 2, '2023-01-01', '9:30', '12:00', '2023-02-10 12.15','И.О. Фамилия');
*/


/*services
DROP TABLE mse;
*/

CREATE TABLE IF NOT EXISTS mse (
  record_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  id_es_buro INTEGER references subdivision(subdivision_id),
  sub_note_id INTEGER references note(note_id),
  s_name VARCHAR(30),
  f_name VARCHAR(30),
  m_name VARCHAR(30),
  birthday DATE,
  time_start_mse TIME,
  time_end_mse TIME
  );

/* example
INSERT INTO mse (id_es_buro, sub_note_id, s_name, f_name, m_name, birthday, time_start_mse, time_end_mse)
VALUES (5, 3, 'Фамилия', 'Имя', 'Отчество', '1990-01-01', '10:00', '12:00');
*/


# --------------------reports--------------------


# journal mse
SELECT
  ROW_NUMBER() OVER(ORDER BY note.note_id desc) as '№ п/п',
  note.iso_number AS 'Вх. № отдела ИСО',
  CONCAT(mse.s_name, ' ', LEFT(mse.f_name, 1), '.', LEFT(mse.m_name, 1), '.') AS 'ФИО освидетельствуемого',
  CONCAT(subdivision.es_or_buro, ' ', subdivision.number_division, ' | ', subdivision.cabinet_mse) AS 'Бюро/ЭС | Помещение №',
  CONCAT(note.date_mse, ' ',  time_start_mse, '-', time_end_mse) AS 'Дата экспертизы, период времени для сохранения (с __ до __)',
  CONCAT(note.current_date_note, ' | ', note.gave) AS 'Сдал дата | ФИО',
  '' AS 'Примечание'
FROM
  mse
INNER JOIN subdivision
  ON mse.id_es_buro = subdivision.subdivision_id
INNER JOIN note
  ON mse.sub_note_id = note.note_id
GROUP BY
  mse.sub_note_id;
  
  
# from operator
SELECT
  *
FROM
  subdivision
WHERE
  