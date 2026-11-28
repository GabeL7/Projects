
using FinancialPlatform.Api.Data;
using FinancialPlatform.Api.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace FinancialPlatform.Api.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class FinancialDocumentsController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public FinancialDocumentsController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<List<FinancialDocument>>> GetAll()
        {
            return await _context.FinancialDocuments
                .AsNoTracking()
                .ToListAsync();
        }

        [HttpGet("{id:int}")]
        public async Task<ActionResult<FinancialDocument>> GetById(int id)
        {
            var document = await _context.FinancialDocuments.FindAsync(id);

            if (document == null)
                return NotFound();

            return Ok(document);
        }

        [HttpPost]
        public async Task<ActionResult<FinancialDocument>> Create(
            CreateFinancialDocumentRequest request)
        {
            var document = new FinancialDocument
            {
                FileName = request.FileName,
                FileSizeBytes = request.FileSizeBytes
            };

            _context.FinancialDocuments.Add(document);
            await _context.SaveChangesAsync();

            return CreatedAtAction(
                nameof(GetById),
                new { id = document.Id },
                document
            );
        }
    }

    public class CreateFinancialDocumentRequest
    {
        [Required]
        [MaxLength(255)]
        public string FileName { get; set; } = string.Empty;

        [Range(0, long.MaxValue)]
        public long FileSizeBytes { get; set; }
    }
}
