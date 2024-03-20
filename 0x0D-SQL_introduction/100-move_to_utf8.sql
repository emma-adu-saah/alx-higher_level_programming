-- Converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- Converts first_table to UTF8
-- Converts field name in first_table to UTF8

ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name TEXT CHARACTER SET = utf8mb4;
