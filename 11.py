'''INSTALLING IMAPALA

1. INSTALL DOCKER

# Update system packages
sudo apt update

# Install prerequisites
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker APT repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index again
sudo apt update

# Install Docker
sudo apt install docker-ce -y

# Start Docker and enable it to launch at boot
sudo systemctl start docker
sudo systemctl enable docker

# (Optional) Add current user to docker group so you don't need sudo
sudo usermod -aG docker $USER

2. docker pull josemyd/all-in-one-impala-kudu

3. docker run -it --name impala-kudu-container josemyd/all-in-one-impala-kudu

4. docker exec -it impala-kudu-container impala-shell
'''

SHOW DATABASES;
CREATE DATABASE sl3_impala;
USE sl3_impala;

CREATE TABLE employees (
    id INT,
    name STRING,
    department STRING,
    salary DOUBLE
)
STORED AS PARQUET;

INSERT INTO employees VALUES
(1, 'Aarav', 'Engineering', 95000),
(2, 'Priya', 'Marketing', 72000),
(3, 'Rohan', 'Finance', 85000),
(4, 'Saanvi', 'Engineering', 98000),
(5, 'Karthik', 'Engineering', 87000),
(6, 'Neha', 'Marketing', 74000);

SELECT * FROM employees WHERE department = 'Engineering';

SELECT * FROM employees WHERE salary > 90000;

SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;

SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

SELECT e.name, e.department, e.salary FROM employees e
JOIN ( SELECT department, AVG(salary) AS avg_salary FROM employees
    GROUP BY department
) dept_avg
ON e.department = dept_avg.department
WHERE e.salary < dept_avg.avg_salary;
