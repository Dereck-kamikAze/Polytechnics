document.addEventListener('DOMContentLoaded', () => {
    const embedConfiguration = {
        type: 'report',
        id: 'your-report-id',
        embedUrl: 'your-embed-url',
        accessToken: 'your-access-token',
        tokenType: models.TokenType.Embed,
        permissions: models.Permissions.All,
    };

    const reportContainer = document.getElementById('reportContainer');
    const report = powerbi.embed(reportContainer, embedConfiguration);
});
