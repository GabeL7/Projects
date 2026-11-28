
using FinancialPlatform.Api.Models;
using Microsoft.EntityFrameworkCore;

namespace FinancialPlatform.Api.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(
            DbContextOptions<ApplicationDbContext> options
        ) : base(options)
        {
        }

        public DbSet<FinancialDocument> FinancialDocuments { get; set; }
            = null!;
    }
}
