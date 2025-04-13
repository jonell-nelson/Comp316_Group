-- Courses with ≥ 50 students
CREATE VIEW PopularCourses AS
SELECT course_id, COUNT(user_id) AS student_count
FROM Enrollment
GROUP BY course_id
HAVING COUNT(user_id) >= 50;

-- Students enrolled in ≥ 5 courses
CREATE VIEW ActiveStudents AS
SELECT user_id, COUNT(course_id) AS course_count
FROM Enrollment
GROUP BY user_id
HAVING COUNT(course_id) >= 5;

-- Lecturers teaching ≥ 3 courses
CREATE VIEW TopLecturers AS
SELECT user_id, COUNT(course_id) AS course_count
FROM Teaching
GROUP BY user_id
HAVING COUNT(course_id) >= 3;

-- Top 10 enrolled courses
CREATE VIEW TopEnrolledCourses AS
SELECT course_id, COUNT(user_id) AS enrollment_count
FROM Enrollment
GROUP BY course_id
ORDER BY enrollment_count DESC
LIMIT 10;

-- Top 10 students by average grade
CREATE VIEW TopStudentsByGrade AS
SELECT ss.user_id, AVG(g.grade) AS avg_grade
FROM Grade g
JOIN StudentSubmission ss ON g.submission_id = ss.submission_id
GROUP BY ss.user_id
ORDER BY avg_grade DESC
LIMIT 10;
