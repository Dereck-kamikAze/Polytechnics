document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const header = document.querySelector('header');
    const searchForm = document.getElementById('search-form');

    // Dark Mode toggle on all pages
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        document.body.style.transition = 'background-color 0.5s ease, color 0.5s ease';
    });

    // Side Bar toggle on all pages
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

    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const title = document.getElementById('job-title').value;
            const location = document.getElementById('job-location').value;
            const salary = document.getElementById('salary').value;
            const company = document.getElementById('company').value;

            fetch(`/api/search?title=${title}&location=${location}&salary=${salary}&company=${company}`)
                .then(response => response.json())
                .then(data => displayJobs(data))
                .catch(error => {
                    console.error('Error fetching jobs:', error);
                });
        });
    }

    function displayJobs(jobs) {
        const tbody = document.querySelector('#job-listings tbody');
        tbody.innerHTML = '';
        jobs.forEach(job => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${job.title || ''}</td>
                            <td>${job.company || ''}</td>
                            <td>${job.location || ''}</td>
                            <td>${job.salary || ''}</td>
                            <td>${job.created_date || ''}</td>
                            <td>${job.closing_date || ''}</td>`;
            tbody.appendChild(tr);
        });
    }
});
