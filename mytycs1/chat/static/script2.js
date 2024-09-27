document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname;

    // Handling sidebar active item
    sidebarItems.forEach(item => {
        const itemLink = item.querySelector('a').getAttribute('href');
        if (currentPath === itemLink) {
            item.setAttribute('id', 'active');
            activeItem = item;
        }
    });

    menuOpen.addEventListener('click', () => {
        sideBar.style.top = '0';
    });

    menuClose.addEventListener('click', () => {
        sideBar.style.top = '-60vh';
    });

    sidebarItems.forEach(element => {
        element.addEventListener('click', () => {
            if (activeItem) {
                activeItem.removeAttribute('id');
            }
            element.setAttribute('id', 'active');
            activeItem = element;
        });
    });

    

    // Function to update dashboard data dynamically
    function updateDashboardData() {
        fetch('/api/get-dashboard-data/')
            .then(response => response.json())
            .then(data => {
                // Update listening progress
                document.getElementById('listening-lessons').textContent = `${data.listening.lessons} Lessons`;
                document.getElementById('listening-progress-bar').style.width = `${data.listening.progress}%`;
                document.getElementById('listening-progress-bar').setAttribute('aria-valuenow', data.listening.progress);

                // Update speaking progress
                document.getElementById('speaking-lessons').textContent = `${data.speaking.lessons} Lessons`;
                document.getElementById('speaking-progress-bar').style.width = `${data.speaking.progress}%`;
                document.getElementById('speaking-progress-bar').setAttribute('aria-valuenow', data.speaking.progress);

                // Update reading progress
                document.getElementById('reading-lessons').textContent = `${data.reading.lessons} Lessons`;
                document.getElementById('reading-progress-bar').style.width = `${data.reading.progress}%`;
                document.getElementById('reading-progress-bar').setAttribute('aria-valuenow', data.reading.progress);

                // Update writing progress
                document.getElementById('writing-lessons').textContent = `${data.writing.lessons} Lessons`;
                document.getElementById('writing-progress-bar').style.width = `${data.writing.progress}%`;
                document.getElementById('writing-progress-bar').setAttribute('aria-valuenow', data.writing.progress);

                // Update upcoming practice sessions
                const upcomingPracticeContainer = document.getElementById('upcoming-practice');
                upcomingPracticeContainer.innerHTML = ''; // Clear old data

                data.upcoming_practices.forEach(practice => {
                    upcomingPracticeContainer.innerHTML += `
                        <div class="item">
                            <div class="left">
                                <div class="icon">
                                    <i class='bx ${practice.icon}'></i>
                                </div>
                                <div class="details">
                                    <h5>${practice.title}</h5>
                                    <p>${practice.time}</p>
                                </div>
                            </div>
                        </div>`;
                });
            })
            .catch(error => console.error('Error fetching dashboard data:', error));
    }

    // Fetch the data every minute
    setInterval(updateDashboardData, 60000);  // Update every 60 seconds
    updateDashboardData();  // Initial fetch on page load
});

// Open and close menu logic (optional if not used elsewhere)
document.getElementById('menu-open').addEventListener('click', function () {
    // logic to open the menu
});

document.getElementById('menu-close').addEventListener('click', function () {
    // logic to close the menu
});
