
using Microsoft.AspNetCore.Mvc;

namespace FinancialPlatform.Api.Controllers
{
    [ApiController] 
    [Route("api/[controller]")] 
    public class HealthController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new
            {
                status = "ok",
                application = "Financial Document Analysis Platform",
                message = "*** Backend API Is Running ***"
            });
        }
    }
}