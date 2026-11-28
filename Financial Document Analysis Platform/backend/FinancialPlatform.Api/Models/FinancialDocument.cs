
using System.ComponentModel.DataAnnotations;

namespace FinancialPlatform.Api.Models
{
    public class FinancialDocument
    {
        public int Id { get; set; }

        [Required]
        [MaxLength(255)]
        public string FileName { get; set; } = string.Empty;

        public long FileSizeBytes { get; set; }

        public DateTime UploadedAtUtc { get; set; } = DateTime.UtcNow;
    }
}
