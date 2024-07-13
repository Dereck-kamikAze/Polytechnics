document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const header = document.querySelector('header');
    const fileInput = document.getElementById('excel-file-input');
    const searchForm = document.getElementById('search-form');
    let jobData = [];

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        document.body.style.transition = 'background-color 0.5s ease, color 0.5s ease';
    });

    sidebarToggle.addEventListener('click', () => {
        const isVisible = sidebar.classList.toggle('visible');
        if (isVisible) {
            sidebar.style.transition = 'transform 0.3s ease';
            header.style.transition = 'left 0.3s ease';
            header.style.left = '250px';
        } else {
            sidebar.style.transition = 'transform 0.3s ease';
            header.style.transition = 'left 0.3s ease';
            header.style.left = '0';
        }
    });

    if (fileInput) {
        fileInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            loadJobsFromFile(file);
        });
    }

    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const title = document.getElementById('job-title').value.toLowerCase();
            const location = document.getElementById('job-location').value.toLowerCase();
            const salary = document.getElementById('salary').value.toLowerCase();
            const companyName = document.getElementById('company-name').value.toLowerCase();
            const filteredJobs = jobData.filter(job => 
                (title === '' || (job['Title'] || '').toLowerCase().includes(title)) &&
                (location === '' || (job['Location'] || '').toLowerCase().includes(location)) &&
                (salary === '' || (job['Salary'] || '').toLowerCase().includes(salary)) &&
                (companyName === '' || (job['Company Name'] || '').toLowerCase().includes(companyName))
            );
            displayJobs(filteredJobs);
        });
    }

    function loadJobsFromFile(file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const data = new Uint8Array(event.target.result);
            const workbook = XLSX.read(data, {type: 'array'});
            const worksheet = workbook.Sheets[workbook.SheetNames[0]];
            const jobs = XLSX.utils.sheet_to_json(worksheet);
            jobData = jobs; // Store loaded jobs data
            displayJobs(jobs);
        };
        reader.readAsArrayBuffer(file);
    }

    function displayJobs(jobs) {
        const tbody = document.querySelector('#job-listings tbody');
        tbody.innerHTML = '';
        jobs.forEach(job => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${job['Title'] || ''}</td>
                            <td>${job['Company Name'] || ''}</td>
                            <td>${job['Location'] || ''}</td>
                            <td>${job['Salary'] || ''}</td>
                            <td>${job['Created Date'] || ''}</td>
                            <td>${job['Closing Date'] || ''}</td>`;
            tbody.appendChild(tr);
        });
    }
});
