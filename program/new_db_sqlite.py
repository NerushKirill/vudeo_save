# start on first run

import sqlite3


conn = sqlite3.connect('../db/journal_video_save')
c = conn.cursor()


c.execute('''
          CREATE TABLE subdivision (
            [subdivision_id] INTEGER NOT NULL PRIMARY KEY,
            [es_or_buro] CHAR(30),
            [number_division] INTEGER(2),
            [supervisor] VARCHAR(90),
            [cabinet_mse] CHAR(10),
            [cam_flow] CHAR(10),
            [download_link] VARCHAR(255)
            );
          ''')


c.execute('''
          CREATE TABLE IF NOT EXISTS note (
            [note_id] INTEGER NOT NULL PRIMARY KEY,
            [iso_number] VARCHAR(10),
            [count_record_day] INTEGER,
            [time_start_mse_day] TIME,
            [time_end_mse_day] TIME,
            [gave] CHAR(90)
            );
          ''')

c.execute('''
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
          ''')

conn.commit()
